from node import Node
from communication import Communication
from election import Election
import time
from threading import Thread
def main():
    # Criar nós
    nodes = [Node(i, 5) for i in range(5)]

    # Comunicação entre nós
    comms = Communication(nodes)

    # Eleições
    election = Election(nodes, comms)

    # Iniciar simulação
    election_thread = Thread(target=election.run)
    election_thread.start()

    try:
        while True:
            time.sleep(5)
            comms.broadcast_append_entries(
                leader=next((n for n in nodes if n.state == "leader"), None),
                entry={"data": "Nova entrada no log!"}
            )
    except KeyboardInterrupt:
        election.stop_event.set()
        election_thread.join()
        print("Simulação encerrada.")

if __name__ == "__main__":
    main()
