import coremltools as ct

mlmodel = ct.models.MLModel("ocr_model.mlmodel")
onnx_model = ct.convert(mlmodel, convert_to="onnx")
onnx_model.save("ocr_model.onnx")
