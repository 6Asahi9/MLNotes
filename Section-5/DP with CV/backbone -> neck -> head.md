Object detection architecture: Backbone → Neck → Head

Exactly — that’s the standard pipeline.

1) Backbone

A CNN like ResNet, MobileNet, EfficientNet, etc.

Its job = extract rich features from the input image

You feed an image → you get feature maps

Think of it like:
Image → “what things exist here in texture/edges/pattern sense"

2) Neck

Combines and refines features from different backbone layers

Examples: FPN (Feature Pyramid Network), PANet, BiFPN

Purpose = make features useful for detection across multiple scales
Because a cat near the camera is huge and far away is tiny — both must be detectable

So Neck = multi-scale feature fusion

3) Head

Takes the refined features and predicts actual results

Usually outputs:

Class probabilities (cat, car, hand sign, etc.)

Bounding box coordinates

Confidence score

This is where detection actually happens
(feature → detection like you wrote)

Summary in one sentence

Backbone extracts features → Neck refines/multiscale them → Head makes final predictions (class + box)
