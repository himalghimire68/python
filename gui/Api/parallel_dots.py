import paralleldots
api_key="NubaG0ojxvvFFXBRhPFXWnVuoDRubxNGzzyg1KVZJgY"
paralleldots.set_api_key(api_key)

print(paralleldots.facial_emotion('1.jpg'))
print(paralleldots.emotion("This good thing is bad"))