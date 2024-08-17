def replace_domain(email,new_domain,old_domain="kaaj.com"):
  a,b = email.split("@")
  if b == new_domain:
    return f"Unchanged: {email}"
  elif b != new_domain or b == old_domain:
    return f"Changed: {a}@{new_domain}"

print(replace_domain("alice@sheba.xyz","sheba.xyz"))