def transcribe2_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech_v1p1beta1 as speech
    #     from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = speech.types.RecognitionAudio(uri=gcs_uri)
    config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        audio_channel_count=2,
        enable_speaker_diarization=True,
        enable_word_time_offsets=True,
        diarization_speaker_count=2,
        max_alternatives=30,
        enable_separate_recognition_per_channel=True,
        language_code='yue-Hant-HK')

    response = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = response.result(timeout=360)

    return response
    
res = transcribe2_gcs("gs://xxxxx")

for resul in res.results:
    print(resul.channel_tag)
    print(resul.alternatives[0].transcript)
