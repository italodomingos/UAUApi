import UAUUpdate
import Email
import traceback
import log

if __name__ == '__main__':
    try:
        UAUUpdate.update_uauapi()
    except Exception as e:
        traceback.print_exc()
        log.write(e)
        msg = f"Erro na atualização do UAUAPI:\n{e}"
        Email.send_message(msg)
