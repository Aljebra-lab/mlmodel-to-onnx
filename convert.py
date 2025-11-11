import coremltools as ct

# Load the Core ML model
mlmodel = ct.models.MLModel("ocr_model.mlmodel")

# Convert to ONNX format
onnx_model = ct.convert(mlmodel, convert_to="onnx")

# Save the ONNX model
onnx_model.save("ocr_model.onnx")
