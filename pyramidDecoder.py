def decode(message_file):
  with open(message_file, 'r') as file:
      lines = file.readlines()

  numbers = []
  decoder = {}
  for line in lines:
      line = line.strip()
      if line:
          parts = line.split()
          number = int(parts[0])
          word = parts[1]
          numbers.append(number)
          decoder[number] = word

  numbers.sort()

  pyramid = []
  block = 1
  while len(numbers) != 0:
    if len(numbers) >= block:
      row = numbers[0:block]
      numbers = numbers[block:]
      pyramid.append(row)
      block += 1


  answerArray = []
  for block in pyramid:
    answerArray.append(decoder[block[-1]])

  return ' '.join(answerArray)

message_file = 'coding_qual_input.txt'
decoded_message = decode(message_file)
print(decoded_message)
