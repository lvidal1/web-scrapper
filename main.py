# from web.Mesajil import Mesajil
# from web.MemoryKings import MemoryKings

from utils.csv_reader import syncFile

# MemoryKingsCall = MemoryKings("https://www.memorykings.pe/resultados/rtx")
# MemoryKingsCall.run()

# MesajilCall = Mesajil(
#     "https://mesajil.com/?s=rtx+tarjeta&post_type=product&dgwt_wcas=1")
# MesajilCall.run()


syncFile("memory_kings.csv")
