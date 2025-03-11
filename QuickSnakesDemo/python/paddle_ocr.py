from paddleocr import PaddleOCR,draw_ocr
import os
import os.path

def predict() -> None:
    ocr = PaddleOCR()
    img_path = os.path.join(os.getcwd(), 'python', 'images', '254.jpg')
    result = ocr.ocr(img_path,rec=False)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)
    
    from PIL import Image
    result = result[0]
    image = Image.open(img_path).convert('RGB')
    im_show = draw_ocr(image, result, txts=None, scores=None, font_path='./simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save('./result.jpg')
    print("Complete")
