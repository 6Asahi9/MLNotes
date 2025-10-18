Summary of key terms:

IoU (Intersection over Union)

Measures how well predicted box overlaps ground truth box.

Used for evaluating localization accuracy.

Precision

Fraction of predicted positives that are correct.

Precision
=
True Positives
True Positives + False Positives
Precision=
True Positives + False Positives
True Positives
	​


Recall

Fraction of actual positives that are correctly detected.

Recall
=
True Positives
True Positives + False Negatives
Recall=
True Positives + False Negatives
True Positives
	​


AP (Average Precision)

Area under precision-recall curve for one class.

Measures overall detection quality for that class.

mAP (Mean Average Precision)

Average of AP across all classes.

Standard metric for object detection performance.

Confidence Score

Each detection comes with a confidence probability.

Thresholding by confidence helps filter weak predictions.
