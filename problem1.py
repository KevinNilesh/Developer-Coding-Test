def reverse_string(s: str) -> str:
  reversed_str = ""
  for char in s:
    reversed_str = char + reversed_str
  return reversed_str

print(reverse_string("hello"))