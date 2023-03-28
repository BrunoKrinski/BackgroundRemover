import flet as ft
from pathlib import PurePath
from rembg import remove, new_session

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
        
        if e.files is None:
            return
        
        total = len(e.files)
        
        pb_container.height = 0
        pb_container.update()
        
        pb.height = 15
        pb.update()
        
        status.value = "Removing Background..."
        status.size = 25
        status.update()
        
        for i, f in enumerate(e.files):
            output_path = f.path.replace('.','_removed_bg.')
            
            input_path = PurePath(f.path)
            output_path = PurePath(output_path)
            
            session = new_session()
            with open(input_path, 'rb') as input:
                with open(output_path, 'wb') as output:
                    input_image = input.read()
                    output_image = remove(input_image, session=session)
                    output.write(output_image)
                        
            image1.src = input_path
            image2.src = output_path
            image1.update()
            image2.update()
                        
            pb.value = i / total
            pb.update()
            
        pb.value = 1
        pb.update()
        
        pb.height = 0
        pb.update()
        
        status.size = 0
        status.update()
            
    select_images_dialog = ft.FilePicker(on_result = select_images_result)
    page.overlay.append(select_images_dialog)
    
    get_files = ft.ElevatedButton(
        content = ft.Text("Select Images!",
            color = ft.colors.BLUE,
            weight = ft.FontWeight.BOLD, 
            size = 40,
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
        height = int(page.height/1.5),
        fit = ft.ImageFit.SCALE_DOWN,
        repeat = ft.ImageRepeat.NO_REPEAT,
        border_radius = ft.border_radius.all(10))
    
    image2 = ft.Image(
        src = 'assets/background.png',
        width = int(page.width/3),
        height = int(page.height/1.5),
        fit = ft.ImageFit.SCALE_DOWN,
        repeat = ft.ImageRepeat.NO_REPEAT,
        border_radius = ft.border_radius.all(10))
    
    pb = ft.ProgressBar(
        width = page.width / 5,
        height = 0,
        color = ft.colors.WHITE)
    
    pb_container = ft.Container(
        height = 15
    )
    
    status = ft.Text(
        "",
        size = 0,
        color = ft.colors.GREEN,
        font_family = "RubikIso")
    
    col1 = ft.Column(
        alignment = ft.MainAxisAlignment.CENTER,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls = [
            get_files,
            pb_container,
            pb,
            status,
        ]
    )
    
    col2 = ft.Column(
        expand = True,
        height = page.height,
        width = int(page.width/3),
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls = [
            space(5),
            col1,
            infos,
        ]
    )
    
    main_row = ft.Row(
        expand = True,
        width = page.width,
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment = ft.CrossAxisAlignment.CENTER,
        controls = [
            image1,
            col2,
            image2,
        ]
    )
        
    main_col = ft.Column(
        expand = True,
        height = page.height,
        #alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls = [
            title,
            main_row,
            #pb,
            #images,
            #space(15),
            #get_files,
            #space(15),
        ]
    )
        
    page.add(main_col)

ft.app(target = main)