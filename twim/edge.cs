private void detectEdgePoint(Bitmap src, CvPoint[] points, out CvPoint[] plateEdgePts, CCTVLocation cctvLocation = CCTVLocation.Top)
        {
            Mat source = OpenCvSharp.Extensions.BitmapConverter.ToMat(src);

            plateEdgePts = new CvPoint[4];

            rowLine = 10;
            colLine = 600;
            // Rule 300
            //inspectionHeight = _inspectionHeight;
            //inspectionWidth = _inspectionWidth;

            Mat lROI1, lROI2;
            Mat lGray1 = new Mat();
            Mat lGray2 = new Mat();

            Mat rRoi1, rRoi2;
            Mat rGray1 = new Mat();
            Mat rGray2 = new Mat();

            // Threshold 값
            int leftThr = 0;
            int rightThr = 0;

            // (180, 255 / 130, 255) / (180, 255 / 160, 255)
            // 전면부 좌측 H빔에 Point 두는 경우 low, high = 100, 160
            if (cctvLocation == CCTVLocation.Top)
            {
                // 전면부(Top)
                leftThr = 50;
                rightThr = 100;
            }
            if (cctvLocation == CCTVLocation.Bottom)
            {
                // 이면부(Bottom)
                leftThr = 100;
                rightThr = 180;
            }

            #region 좌 1 구역 범위 지정
            // ROI 1구역 범위 지정 및 생성
            // MEMO : 총 4개의 points 어떻게 받아오는지 질문
            Range rowRange1 = new Range(points[0].Y, points[0].Y + this.rowLine);
            Range colRange1 = new Range(points[0].X - this.colLine, points[0].X);
            lROI1 = source.SubMat(rowRange1, colRange1);
            #endregion

            #region 좌 2 구역 범위 지정
            Range rowRange2 = new Range(points[1].Y, points[1].Y + this.rowLine);
            Range colRange2 = new Range(points[1].X - this.colLine, points[1].X);
            lROI2 = source.SubMat(rowRange2, colRange2);
            #endregion

            #region 우 1 구역 범위 지정
            // ROI 3구역(우 1) 범위 지정 및 생성
            Range rRowRange1 = new Range(points[2].Y, points[2].Y + this.rowLine);
            Range rColRange1 = new Range(points[2].X, points[2].X + this.colLine);
            rRoi1 = source.SubMat(rRowRange1, rColRange1);
            #endregion

            #region 우 2 구역 범위 지정
            Range rRowRange2 = new Range(points[3].Y, points[3].Y + this.rowLine);
            Range rColRange2 = new Range(points[3].X, points[3].X + this.colLine);
            rRoi2 = source.SubMat(rRowRange2, rColRange2);
            #endregion

            // 입력 영상 BGR -> Gray
            Cv2.CvtColor(lROI1, lGray1, ColorConversionCodes.BGR2GRAY);
            Cv2.CvtColor(lROI2, lGray2, ColorConversionCodes.BGR2GRAY);
            Cv2.CvtColor(rRoi1, rGray1, ColorConversionCodes.BGR2GRAY);
            Cv2.CvtColor(rRoi2, rGray2, ColorConversionCodes.BGR2GRAY);

            switch (cctvLocation)
            {
                case CCTVLocation.Top:
                    break;
                case CCTVLocation.Bottom:
                    break;
            }

            #region 강판 Edge 부분 찾기 - 좌 1
            ////////////////////////////////////////
            /// 1. 강판 Edge 부분 찾기
            ////////////////////////////////////////
            // 입력영상 이진화(좌 1)
            using (Mat bin = new Mat())
            using (Mat aBin = new Mat())
            {
                bool findEdge = false;
                // Edge 탐지 후보군 영역 내부 평균 픽셀 값
                Cv2.Threshold(lGray1, bin, leftThr, 255, ThresholdTypes.Binary | ThresholdTypes.Otsu);
                Mat element = Cv2.GetStructuringElement(MorphShapes.Ellipse, new OpenCvSharp.Size(3, 3));
                //Cv2.MorphologyEx(bin, bin, MorphTypes.Open, element, iterations: 1);
                if(cctvLocation == CCTVLocation.Bottom)
                    Cv2.Dilate(bin, bin, element, new CvPoint(0, 0), 1);

                // 이진화 영상 횡 라인 값 검사(강판 Edge 부분 찾기)
                for (int col = bin.Cols - 1; col > 0; col--)
                {
                    byte val = bin.At<byte>(0, col);

                    if (val == 0)
                    {
                        plateEdgePts[0] = new CvPoint(col + 3, points[0].Y);
                        //plateEdgePt1 = new CvPoint(col - 10, points[0].Y);
                        findEdge = true;
                        break;
                    }
                }

                //Cv2.ImShow("gray-L1", lGray1);
                //Cv2.ImShow("bin-L1", bin);
                //Cv2.WaitKey(1);
            }
            #endregion

            #region 강판 Edge 부분 찾기 - 좌 2
            using (Mat bin = new Mat())
            {
                bool findEdge = false;
                Cv2.Threshold(lGray2, bin, leftThr, 255, ThresholdTypes.Binary | ThresholdTypes.Otsu);
                Mat element = Cv2.GetStructuringElement(MorphShapes.Ellipse, new OpenCvSharp.Size(3, 3));
                Cv2.Dilate(bin, bin, element, new CvPoint(0, 0), 1);

                for (int col = bin.Cols - 1; col > 0; col--)
                {
                    byte val = bin.At<byte>(0, col);

                    if (val == 0)
                    {
                        plateEdgePts[1] = new CvPoint(col + 3, points[1].Y);
                        findEdge = true;
                        break;
                    }
                }

                //Cv2.ImShow("bin-L2", bin);
                //Cv2.WaitKey(1);
            }
            #endregion

            #region 강판 Edge 부분 찾기 - 우 1
            using (Mat bin = new Mat())
            {
                bool findEdge = false;
                Cv2.Threshold(rGray1, bin, rightThr, 255, ThresholdTypes.Binary | ThresholdTypes.Otsu);
                Mat element = Cv2.GetStructuringElement(MorphShapes.Ellipse, new OpenCvSharp.Size(3, 3));
                if (cctvLocation == CCTVLocation.Bottom)
                    Cv2.Dilate(bin, bin, element, new CvPoint(0, 0), 2);

                // 이진화 영상 횡 라인 값 검사(강판 Edge 부분 찾기)
                //for (int row = canny.Cols; row > 0; row--)
                for (int col = 0; col < bin.Cols; col++)
                //for (int i = bin.Cols; i > 0; i--)
                {
                    byte val = bin.At<byte>(0, col);
                    if (val == 0)
                    {
                        plateEdgePts[2] = new CvPoint(points[2].X + col - 3, points[2].Y);
                        //plateEdgePt3 = new CvPoint(col, Point[2].Y);

                        findEdge = true;
                        break;
                    }
                }
                //Cv2.ImShow("grayR1", rGray1);
                //Cv2.ImShow("binR1", bin);
                //Cv2.WaitKey(1);
            }
            #endregion

            #region 강판 Edge 부분 찾기 - 우 2
            using (Mat bin = new Mat())
            {
                bool findEdge = false;
                Cv2.Threshold(rGray2, bin, rightThr, 255, ThresholdTypes.Binary | ThresholdTypes.Otsu);
                Mat element = Cv2.GetStructuringElement(MorphShapes.Ellipse, new OpenCvSharp.Size(3, 3));
                if(cctvLocation == CCTVLocation.Bottom)
                    Cv2.Dilate(bin, bin, element, new CvPoint(0, 0), 2);

                // 이진화 영상 횡 라인 값 검사(강판 Edge 부분 찾기)
                //for (int row = canny.Cols; row > 0; row--)
                for (int col = 0; col < bin.Cols; col++)
                //for (int i = bin.Cols; i > 0; i--)
                {
                    byte val = bin.At<byte>(0, col);
                    if (val == 0)
                    {
                        plateEdgePts[3] = new CvPoint(points[3].X + col - 3, points[3].Y); ;
                        //plateEdgePt3 = new CvPoint(col, Point[2].Y);

                        findEdge = true;
                        break;
                    }
                }
                //Cv2.ImShow("grayR2", rGray2);
                //Cv2.ImShow("binR2", bin);
                //Cv2.WaitKey(1);
            }
            #endregion
        }
        #endregion