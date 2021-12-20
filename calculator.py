def add(n1,n2):
  return n1 + n2
def substract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2
num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))

operators = {
  "+":add,
  "-":substract,
  "*":multiply,
  "/":divide,
}
for symbol in operators:
  print(symbol)
operator_symbol = input("Select anyone operations from above: ")
calculator = operators[operator_symbol]
answer = round(calculator(num1,num2),2)
print(f" {num1} {operator_symbol} {num2} = {answer}")

