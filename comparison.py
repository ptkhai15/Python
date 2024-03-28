"John" == "John" /True
"John" == "David" /False
5 == 7 /False
9 == "John" /False
"John" != "John" /False
"John" != "David" /True
"John" < "John" /False
"John" < "David" /False
5 < 7 /True
9 < "John" /error
"John" > "John" /False
"John" > "David" /True
"John" <= "John" /True
5 == 5 and "John" < "David" /False
"Jack" >= "David" and "John" == "John" /True
5 == 5 or "John" < "David" /True
not "John" <= "John" /False

