import subprocess

def get_wifi_profiles():
    try:
        # Obtém a lista de perfis de redes Wi-Fi
        data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
        print("Saída do comando 'netsh wlan show profiles':")
        print("\n".join(data))
        profiles = [i.split(":")[1].strip() for i in data if "All User Profile" in i]
        print("Perfis encontrados:", profiles)
        return profiles
    except subprocess.CalledProcessError as e:
        print(f"Erro ao obter perfis de redes Wi-Fi: {e}")
        return []

def get_wifi_password(profile):
    try:
        results = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode("utf-8").split("\n")
        print(f"Saída do comando 'netsh wlan show profile {profile} key=clear':")
        print("\n".join(results))
        passwords = [b.split(":")[1].strip() for b in results if "Key Content" in b]
        return passwords[0] if passwords else None
    except subprocess.CalledProcessError as e:
        print(f"Erro ao obter senha para o perfil {profile}: {e}")
        return None

def main():
    profiles = get_wifi_profiles()
    if not profiles:
        print("Nenhum perfil de rede Wi-Fi encontrado.")
        return

    for profile in profiles:
        password = get_wifi_password(profile)
        print("{:<30}|  {:<}".format(profile, password if password else "Senha não encontrada"))

if __name__ == "__main__":
    main()
