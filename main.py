import cv2
import pytesseract

# Configuração do pytesseract (ajuste conforme necessário)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Lista de placas
lista_de_placas = ["ABC123", "XYZ789", "123ABC", "789XYZ", "BRA2E19"]


def capture_and_ocr():
    # Inicializar a câmera (0 indica a câmera padrão)
    cap = cv2.VideoCapture(0)

    # Definir a resolução desejada (por exemplo, 640x480)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Aguardar um breve momento para a câmera ajustar as configurações
    cv2.waitKey(1000)

    while True:
        # Capturar frame da câmera
        ret, frame = cap.read()

        # Realizar OCR na imagem
        text = pytesseract.image_to_string(frame)

        # Exibir o texto na janela
        print("Texto da placa:", text)

        # Verificar se a placa reconhecida está na lista
        if any(placa in text for placa in lista_de_placas):
            print("Placa encontrada:", text)
            break
        else:
            print("Placa não encontrada")

        # Exibir o frame com o texto (você pode personalizar essa parte conforme necessário)
        cv2.imshow('Camera OCR', frame)

        # Encerrar o loop ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar a câmera e fechar a janela
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_and_ocr()
