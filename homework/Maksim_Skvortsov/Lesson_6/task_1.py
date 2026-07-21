text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
new_text = ""
for i in text.split():
    # print(i) #выводим каждый элемент
    new_text = new_text + i + "ing "
    # print("Сейчас строка выглядит так:", new_text)
    new_text = new_text.replace(",ing", "ing,")
    new_text = new_text.replace(".ing", "ing.")
print(new_text)
