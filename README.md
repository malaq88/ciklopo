
**Ciklopo** - Reconhecimento de Placas de Veículos com OCR

Descrição:
O aplicativo Ciklopo utiliza a biblioteca OpenCV e o mecanismo de reconhecimento óptico de caracteres (OCR) fornecido pelo Tesseract para realizar a captura e análise de placas de veículos em tempo real a partir da câmera padrão do dispositivo. O objetivo principal é identificar se a placa capturada está presente em uma lista predefinida de placas.

Configuração:
Antes de executar o aplicativo, certifique-se de ter o Tesseract OCR instalado no seu sistema. Para instalar no Linux, utilize o comando: sudo apt-get install tesseract-ocr. Além disso, é necessário ajustar o caminho do executável do Tesseract na configuração do pytesseract, indicado pela variável tesseract_cmd.

Lista de Placas:
O aplicativo possui uma lista predefinida de placas que são consideradas como "placas válidas". Essa lista é representada pela variável lista_de_placas, e você pode personalizá-la conforme necessário, adicionando ou removendo placas.

Funcionamento:

Ao iniciar o aplicativo, a câmera padrão é inicializada.
O aplicativo entra em um loop contínuo de captura de frames da câmera.
Cada frame capturado é submetido ao OCR para reconhecimento de texto.
O texto reconhecido é exibido na janela do console.
O aplicativo verifica se a placa reconhecida está na lista de placas predefinida.
Se a placa for encontrada, o aplicativo exibe uma mensagem indicando a placa reconhecida e encerra o processo.
Caso contrário, o aplicativo continua a busca e exibe uma mensagem informando que a placa não foi encontrada.
O frame da câmera, com o texto reconhecido, é exibido em uma janela separada chamada 'Camera OCR'.
O loop pode ser encerrado a qualquer momento pressionando a tecla 'q'.
Instruções:
Certifique-se de ter todas as dependências instaladas e o Tesseract configurado corretamente. Execute o aplicativo e direcione a câmera para a placa de um veículo. Pressione 'q' a qualquer momento para encerrar a aplicação.

Observações:

Personalize a lista de placas conforme necessário para atender aos requisitos específicos.
Modifique a exibição da janela 'Camera OCR' de acordo com as preferências de interface do usuário.
Este aplicativo serve como uma base para projetos de reconhecimento de placas e pode ser expandido com funcionalidades adicionais, como integração com bancos de dados ou notificações.
