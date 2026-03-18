# ============================================
# 👑 ROYAL EVEN NUMBERS CHALLENGE 👑
# ============================================

def even(li):
    """👑 Royal function to discover even numbers in the kingdom 👑"""
    print("\n" + "👑" * 50)
    print("👑              ROYAL EVEN NUMBERS DISCOVERY")
    print("👑" * 50)
    
    evens = []
    print("\n📜 Royal Census of Numbers:")
    print("-" * 40)
    
    for i in li:
        if i % 2 == 0:
            print(f"  ✦ {i} ← 👑 EVEN NUMBER (Knighted!)")
            evens.append(i)
        else:
            print(f"    {i}")
    
    print("-" * 40)
    print(f"\n👑 Royal Statistics:")
    print(f"  ✧ Total subjects in kingdom: {len(li)}")
    print(f"  ✧ Even numbers discovered: {len(evens)}")
    
    if evens:
        print(f"  ✧ Smallest even: {min(evens)} 👶")
        print(f"  ✧ Largest even: {max(evens)} 👑")
        print(f"  ✧ Sum of all evens: {sum(evens)} 💰")
        print(f"  ✧ Royal evens: {evens}")
    
    print("\n" + "👑" * 50)
    print("👑           LONG LIVE THE EVEN NUMBERS!")
    print("👑" * 50)

# Royal test data
li = [1, 2, 3, 6, 5, 4, 7, 8, 9, 10]

# Summon the royal function
even(li)