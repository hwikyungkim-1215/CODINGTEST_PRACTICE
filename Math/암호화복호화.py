def encrypt(plainString, n):
  result = ""
  for i in range(len(plainString)):
    char = plainString[i]
    if (char.isspace()):
      result += " "
    else:
      if (char.isupper()):
        result += chr((ord(char) + n - 65) % 26 + 65)
      else:
        result += chr((ord(char) + n - 97) % 26 + 97)
  return result

def decrypt(encryptedString, n):
  result = ""
  for i in range(len(encryptedString)):
    char = encryptedString[i]
    if (char.isspace()):
      result += " "
    else:
      if (char.isupper()):
        result += chr((ord(char) - n - 65) % 26 + 65)
      else:
        result += chr((ord(char) - n - 97) % 26 + 97)
  return result


def main():
  number = int(input("Input Number > "))
  print(decrypt("HTRUZYJWXJHZWNYD", number))
  print(decrypt(encrypt("HTRUZYJWXJHZWNYD", number), number))

if __name__ == "__main__":
  main()