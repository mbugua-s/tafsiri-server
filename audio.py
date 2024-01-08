import html
from google.cloud import texttospeech

def text_to_speech(text: str, outfile: str) -> str:
    escaped_lines = html.escape(text)

    ssml = "<speak>{}</speak>".format(
        escaped_lines.replace("\n", '\n<break time="2s"/>')
    )

    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(ssml=ssml)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    request = texttospeech.SynthesizeSpeechRequest(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    response = client.synthesize_speech(request=request)

    with open(outfile, "wb") as out:
        out.write(response.audio_content)
        print("Audio content written to file " + outfile)