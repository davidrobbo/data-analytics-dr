Bayes Theorem

P(A|B) =

(P(A) * P(B|A)) / P(B)

Named 'Naive' as it considers inputs as independent (which is unrealistic)

The Probability of A occurring given B occured =
How often A happens times by the probability of B given A
divided by the probability of B occurring

Consider the case of a new disease diagnosis test and the following info:
The test diagnoses non-positive patients positively 5% of the time (FP)

P(disease) = 0.01 (1 in a 100)
P(positive|disease) = 0.9 (if someone has disease, it will diagnose correct 90% of the time)

Population = 10000
disease total = 100
disease correctly diagnosed (positive) = 90
Non-disease = 9900
disease wrongly diagnosed (positive) = 495
P(positive) = (495+90)/10000 = 0.0585

P(disease|positive) =

(P(disease)[0.01] * P(positive|disease)[0.9]) / P(disease)[0.0585]

= 0.154
Therefore, if you test positive for disease, then there is only a 15.4% chance it diagnosed correctly (in this fictional example)


