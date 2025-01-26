### Простая реализация консольного чата

Перед вами простая реализация консольного чата, где вы можете запустить серверную программу (`server.py`) на localhost (127.0.0.1) и на указанном порту (9999) для приема сообщений от клиентов. Вы можете запустить `client1.py` несколько раз, создавая несколько клиентов.

После получения сообщения от клиента, сервер перешлет его всем подключенным клиентам (broadcast), кроме отправителя.

---

**!Проект находится в разработке!**  
Не стесняйтесь модифицировать исходный код под свои нужды.

---

### Как развернуть сервер и клиентов:

1. **Запустите сервер**, используя команду:

   ```
   python server.py
   ```

2. **Запустите клиентов** (один терминал - один клиент):

   ```
   python client1.py
   ```

3. **Тестируйте :3**

---

### Simple Console Chat Implementation

This is a simple implementation of a console chat, where you can run the server program (`server.py`) on localhost (127.0.0.1) and the specified port (9999) to receive messages from clients. You can run `client1.py` multiple times, creating multiple clients.

After receiving a message from a client, the server will forward the message to all connected clients (broadcast), except for the sender.

---

**!The project is under development!**  
Feel free to modify the source code to suit your needs.

---

### How to Deploy the Server and Clients:

1. **Start the server** by running the following command:

   ```
   python server.py
   ```

2. **Run the clients** (one terminal - one client):

   ```
   python client1.py
   ```

3. **Test it out** :3
