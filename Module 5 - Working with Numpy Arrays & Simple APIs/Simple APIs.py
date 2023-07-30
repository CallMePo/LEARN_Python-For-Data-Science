from ibm_watson import SpeechToTextV1
url_s2t="https://stream.watsonplatform.net/speech-to-text/api"
iam_apikey_s2t="EOeiZxxxDxV2xxxxxxxxxxxjYen9SKARKW-"
s2t = SpeechToTextV1(iam_apikey=iam_apikey_s2t, url=url_s2t)
