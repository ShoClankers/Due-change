
total_cost = float(input("Enter total cost: "))
amount_paid = float(input("Enter amount paid: "))

change = amount_paid - total_cost

if change > 0:
    print(f"Change to give back: ${change:.2f}")
elif change == 0:
    print("Exact payment. No change needed.")
else:
    print(f"Customer still owes: ${abs(change):.2f}")