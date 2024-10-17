import flet as ft


def main(page: ft.Page):
#establecer tamaño de pantalla

    page.window_width=800
    page.window_height=800
    
    page.bgcolor="pink"
    page.title="mitlan"
    page.fgcolor="red"
    
    Intro=ft.Audio(src="Intro.mp3",volumen=1,balance=0)
    page.overlay.append(Intro)
    
    primernivel=ft.Audio(src="Primer_nivel.mp3",volumen=1,balance=0)
    page.overlay.append(primernivel)
    
    segundonivel=ft.Audio(src="segundo_nivel.mp3",volumen=1,balance=0)
    page.overlay.append(segundonivel)
    
    tercernivel=ft.Audio(src="tercer_nivel.mp3",volumen=1,balance=0)
    page.overlay.append(tercernivel)
    
    cuartonivel=ft.Audio(src="cuarto_nivel.mp3",volumen=1,balance=0)
    page.overlay.append(cuartonivel)
    
    quintonivel=ft.Audio(src="quinto_nivel.mp3",volumen=1,balance=0)
    page.overlay.append(quintonivel)
    
    sextonivel=ft.Audio(src="sexto_nivel.mp3",volumen=1,balance=0)
    page.overlay.append(sextonivel)
    
    septimonivel=ft.Audio(src="septimo_nivel.mp3",volumen=1,balance=0)
    page.overlay.append(septimonivel)
    
    octavonivel=ft.Audio(src="octavo_nivel.mp3",volumen=1,balance=0)
    page.overlay.append(octavonivel)
    
    novenonivel=ft.Audio(src="noveno_nivel.mp3",volumen=1,balance=0)
    page.overlay.append(novenonivel)
    
#se crea la interfaz

    btnIntro=ft.FilledButton(tex="escucha el Intro", disabled=False)
    
    btnnivel1=ft.ElevatedButton(text="primer nivel")
    img1=ft.Image(src="primer-nivel.jpeg",width=150,height=150)
    
    btnnivel2=ft.ElevatedButton(text="segundo nivel")
    img2=ft.Image(src="segundo-nivel.jpeg",width=150,height=150)

    btnnivel3=ft.ElevatedButton(text="tercer nivel")
    img3=ft.Image(src="tercer-nivel.png",width=150,height=150)

    btnnivel4=ft.ElevatedButton(text="cuarto nivel")
    img4=ft.Image(src="cuarto-nivel.jpeg",width=150,height=150)

    btnnivel5=ft.ElevatedButton(text="quinto nivel")
    img5=ft.Image(src="quinto-nivel.jpeg",width=150,height=150)

    btnnivel6=ft.ElevatedButton(text="sexto nivel")
    img6=ft.Image(src="sexto-nivel.jpeg",width=150,height=150)

    btnnivel7=ft.ElevatedButton(text="septimo nivel")
    img7=ft.Image(src="septimo-nivel.jpeg",width=150,height=150)

    btnnivel8=ft.ElevatedButton(text="octavo nivel")
    img8=ft.Image(src="octavo-nivel.png",width=150,height=150)

    btnnivel9=ft.ElevatedButton(text="noveno nivel")
    img9=ft.Image(src="noveno-nivel.jpeg",width=150,height=150)

    page.add(
        ft.Row(
            alignment="start",
            controls=[btnIntro]
        ),
        ft.Column(
            alignment="CENTER",
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    alignment="CENTER",
                    controls=[btnnivel1,img1]
                ),
                ft.Column(
                    alignment="CENTER",
                    controls=[btnnivel2,img2]
                ),
                ft.Column(
                    alignment="CENTER",
                    controls=[btnnivel3,img3]
                )
            ]
        )
    )

ft.app(main)
