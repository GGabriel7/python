import pygame
import time

# Inicialize o Pygame
pygame.init()

# Caminho para o arquivo de áudio
audio_path = "audio.mp3.opus"

# Inicialize o mixer de áudio do Pygame
pygame.mixer.init()

# Carregue o arquivo de áudio
pygame.mixer.music.load(audio_path)

# Reproduza o áudio
pygame.mixer.music.play()

# Aguarde até que a reprodução termine (ou use eventos para controlar)
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Finalize o Pygame
pygame.quit()
