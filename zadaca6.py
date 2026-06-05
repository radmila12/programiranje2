
def ispisi_unazad_verzija(string):
    if len(string) == 0:
        return
    print(string[-1], end="")

  def ispisi_unazad_verzija1(string[:-1])
def ispisi_unazad_verzija2(string):

    if len(string) == 0:
        return
    ispisi_unazad_verzija2(string[1:])
    print(string[0], end=
          
if __name__ == "__main__":
    
    unos_string = "SUM"
    print(f"Originalni string: {unos_string}")
    print("-" * 30)
    
    print("Ispis pomoću Verzije 1 (od kraja): ", end="")
    ispisi_unazad_verzija1(unos_string)
    print()  # Prazan ispis samo za prelazak u novi red
    print("Ispis pomoću Verzije 2 (od početka): ", end="")
    ispisi_unazad_verzija2(unos_string)
    print()  # Prazan ispis samo za prelazak u novi red
    
    print("-" * 30)