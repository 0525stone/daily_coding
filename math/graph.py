"""
260307 사업계획서에 추가할 그래프를 그려보려고 하는 중...

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyArrowPatch
import matplotlib.patheffects as pe

# ── 한글 폰트 설정 ──────────────────────────────────────────────
import matplotlib
import subprocess, os

# 나눔고딕 설치 시도
try:
    subprocess.run(["fc-list"], capture_output=True)
    fonts = subprocess.run(["fc-list", ":lang=ko"], capture_output=True, text=True).stdout
    if "Nanum" not in fonts:
        subprocess.run(["apt-get", "install", "-y", "fonts-nanum"], capture_output=True)
        matplotlib.font_manager._load_fontmanager(try_read_cache=False)
except:
    pass

from matplotlib import font_manager
nanum = [f.fname for f in font_manager.fontManager.ttflist if "Nanum" in f.name]
if nanum:
    plt.rcParams["font.family"] = font_manager.FontProperties(fname=nanum[0]).get_name()
else:
    plt.rcParams["font.family"] = "DejaVu Sans"

plt.rcParams["axes.unicode_minus"] = False

# ── 시간축 & 가상 신호 생성 ─────────────────────────────────────
np.random.seed(42)
t = np.linspace(0, 10, 1000)

def smooth_step(t, on, off, rise=0.3):
    """부드러운 ON/OFF 전환"""
    s = np.zeros_like(t)
    for i in range(len(t)):
        if t[i] < on:
            s[i] = 0
        elif t[i] < on + rise:
            s[i] = ((t[i] - on) / rise) ** 2
        elif t[i] < off:
            s[i] = 1
        elif t[i] < off + rise:
            s[i] = 1 - ((t[i] - off) / rise) ** 2
        else:
            s[i] = 0
    return s

# 개별 기기 신호
noise = lambda amp: amp * np.random.randn(len(t))

ac      = smooth_step(t, 1.0, 8.5) * 1500 + noise(15)   # 에어컨
fridge  = (smooth_step(t, 0.5, 3.0) + smooth_step(t, 5.5, 9.0)) * 120 + noise(5)  # 냉장고
washer  = smooth_step(t, 2.0, 6.0) * 500 + noise(10)    # 세탁기
light   = smooth_step(t, 0.2, 9.5) * 60  + noise(3)     # 조명

# 총 신호 (합산)
total = ac + fridge + washer + light + noise(20)

# ── 색상 & 기기 정보 ───────────────────────────────────────────
devices = [
    ("Total Power Signal", total,  "#2C3E50", "-",  True),
    ("Air Conditioner",    ac,     "#E74C3C", "--", False),
    ("Refrigerator",       fridge, "#3498DB", "--", False),
    ("Washing Machine",    washer, "#2ECC71", "--", False),
    ("Lighting",           light,  "#F39C12", "--", False),
]

# ══════════════════════════════════════════════════════════════
# Figure 1 : 합쳐진 신호 + 분해된 신호를 한 화면에
# ══════════════════════════════════════════════════════════════
fig1, axes = plt.subplots(
    len(devices), 1,
    figsize=(13, 10),
    sharex=True,
    gridspec_kw={"hspace": 0.08}
)
fig1.patch.set_facecolor("#F8F9FA")

for ax, (label, sig, color, ls, is_total) in zip(axes, devices):
    ax.set_facecolor("#FFFFFF" if not is_total else "#EEF2FF")
    ax.plot(t, sig, color=color, linewidth=2.2 if is_total else 1.6,
            linestyle="-" if is_total else ls, alpha=0.95)
    ax.fill_between(t, sig, alpha=0.12, color=color)

    # 레이블 박스
    ax.text(
        -0.01, 0.5, label,
        transform=ax.transAxes,
        ha="right", va="center",
        fontsize=11, fontweight="bold" if is_total else "normal",
        color=color,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color, lw=1.5, alpha=0.9)
    )

    ax.set_ylabel("W", fontsize=9, color="#666666")
    ax.tick_params(labelsize=8, colors="#555555")
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#CCCCCC")
    ax.grid(axis="y", linestyle=":", alpha=0.4, color="#AAAAAA")

    # 총 신호에 화살표 + 안내 텍스트
    if is_total:
        ax.set_title(
            "NILM Signal Decomposition — Separating Appliances from One Power Line",
            fontsize=14, fontweight="bold", pad=12, color="#2C3E50"
        )
        ax.annotate(
            "AI decomposes\nthis signal below",
            xy=(5.0, total[500]), xytext=(6.8, total[500] * 1.05),
            fontsize=9, color="#555555",
            arrowprops=dict(arrowstyle="->", color="#888888", lw=1.4),
        )

axes[-1].set_xlabel("Time (min)", fontsize=10, color="#444444")

# 하단 설명
fig1.text(
    0.5, 0.01,
    "※ AI (NILMFormer) decomposes the total power signal from a single meter into per-appliance consumption.",
    ha="center", fontsize=9, color="#888888", style="italic"
)

plt.savefig("./nilm_combined.png", dpi=150, bbox_inches="tight",
             facecolor=(1, 1, 1, 0.5))
plt.close()
print("✅ nilm_combined.png 저장 완료")


# ══════════════════════════════════════════════════════════════
# Figure 2 : 기기별 개별 그래프 (카드 스타일)
# ══════════════════════════════════════════════════════════════
device_list = devices[1:]   # 총 신호 제외
n = len(device_list)

fig2, axes2 = plt.subplots(1, n, figsize=(16, 4), sharey=False)
fig2.patch.set_facecolor("#F0F4F8")

for ax, (label, sig, color, ls, _) in zip(axes2, device_list):
    # 카드 배경
    ax.set_facecolor("#FFFFFF")
    for spine in ax.spines.values():
        spine.set_edgecolor(color)
        spine.set_linewidth(2)

    ax.plot(t, sig, color=color, linewidth=2, alpha=0.95)
    ax.fill_between(t, sig, alpha=0.18, color=color)

    # Avg 소비전력 표시
    avg = np.mean(sig[sig > 20]) if np.any(sig > 20) else 0
    ax.axhline(avg, color=color, linewidth=1, linestyle=":", alpha=0.6)
    ax.text(9.8, avg + 10, f"Avg\n{avg:.0f}W",
            fontsize=7.5, color=color, ha="right", va="bottom")

    ax.set_title(label, fontsize=13, fontweight="bold", color=color, pad=10)
    ax.set_xlabel("Time (min)", fontsize=9, color="#666666")
    ax.set_ylabel("Power (W)", fontsize=9, color="#666666")
    ax.tick_params(labelsize=8)
    ax.grid(axis="y", linestyle=":", alpha=0.35)

fig2.suptitle(
    "Per-Appliance Decomposed Power Signals",
    fontsize=15, fontweight="bold", color="#2C3E50", y=1.03
)
fig2.text(
    0.5, -0.04,
    "Each graph shows the power consumption of an appliance separated by AI from the total signal.",
    ha="center", fontsize=9, color="#888888", style="italic"
)

plt.tight_layout(pad=2.0)
plt.savefig("./nilm_individual.png", dpi=150, bbox_inches="tight",
             facecolor=(1, 1, 1, 0.5))
plt.close()
print("✅ nilm_individual.png 저장 완료")
