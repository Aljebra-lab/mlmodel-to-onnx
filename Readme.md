# Core ML to ONNX Converter

This repo uses GitHub Actions to convert a `.mlmodel` file into ONNX format using a free macOS runner.

## How to use

1. Upload your `.mlmodel` file as `ocr_model.mlmodel` to the root of this repo.
2. Go to the **Actions** tab in GitHub.
3. Select **Convert Core ML to ONNX** workflow.
4. Click **Run workflow**.
5. After completion, download the `onnx-model` artifact.

## Notes

- This uses `coremltools` on macOS.
- ONNX model will be saved as `ocr_model.onnx`.