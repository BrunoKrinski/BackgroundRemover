import flet as ft
from rembg import remove

def main(page: ft.Page):
    page.title = "Background Remover!"
    page.window_maximized = True
    page.theme_mode = "DARK"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = False
    
    page.fonts = {
        "RubikIso": "fonts/RubikIso-Regular.ttf"
    }
    
    space = lambda height = 0 : ft.Container(height = height,
                                             padding = 0,
                                             margin = 0)
    
    def open_image(image_path):
        return ft.Image(
            src = image_path,
            width = 200,
            height = 400,
            fit = ft.ImageFit.COVER,
            repeat = ft.ImageRepeat.NO_REPEAT,
            border_radius = ft.border_radius.all(10))
    
    def select_images_result(e: ft.FilePickerResultEvent):
        for f in e.files:
            output_path = f.path.replace('.','_removed_bg.')
            with open(f.path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)
            
            image1.src = f.path
            image2.src = output_path
            image1.update()
            image2.update()

    select_images_dialog = ft.FilePicker(on_result = select_images_result)
    page.overlay.append(select_images_dialog)
    
    get_files = ft.ElevatedButton(
        content = ft.Text("Select Images!",
            color = ft.colors.BLUE,
            weight = ft.FontWeight.BOLD, 
            size = 50,
            font_family = "RubikIso"),
        on_click = lambda _: select_images_dialog.pick_files(allow_multiple = True)
    )
    
    title = ft.Text(
        "Pinterest Downloader!", 
        size = 100,
        color = ft.colors.BLUE,
        weight = ft.FontWeight.BOLD,
        font_family = "RubikIso")
    
    developed = ft.Text(
        "Developed by War Machine!",
        color = ft.colors.RED,
        weight = ft.FontWeight.BOLD, 
        size = 25,
        font_family = "RubikIso")
    
    github_button = ft.TextButton(
        content = ft.Text("GitHub!", 
            size = 20,
            font_family = "RubikIso",
            color = ft.colors.WHITE),
        on_click = lambda _ : 
            page.launch_url('https://github.com/BrunoKrinski'))
    
    infos = ft.Column(
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls = [
            developed, github_button
        ]
    )
    
    image1 = ft.Image(
        src = 'assets/background.png',
        width = int(page.width/3),
        height = int(page.height/3),
        fit = ft.ImageFit.COVER,
        repeat = ft.ImageRepeat.NO_REPEAT,
        border_radius = ft.border_radius.all(10))
    
    image2 = ft.Image(
        src = 'assets/background.png',
        width = int(page.width/3),
        height = int(page.height/3),
        fit = ft.ImageFit.COVER,
        repeat = ft.ImageRepeat.NO_REPEAT,
        border_radius = ft.border_radius.all(10))
    
    row1 = ft.Row(
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
        controls = [
            image1,
            get_files,
            image2
        ]
    )
        
    main_col = ft.Column(
        expand = True,
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls = [
            title,
            row1,
            #images,
            #space(15),
            #get_files,
            #space(15),
            infos,
        ]
    )
        
    page.add(main_col)

ft.app(target = main)