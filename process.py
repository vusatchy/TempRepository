#'load: -1' this mean load last model from ckpt folder
options = {"model": "cfg/yolo_custom.cfg",
           "load": -1,
           "gpu": 0.9}
tfnet2 = TFNet(options)

#loading last model from ckpt
tfnet2.load_from_ckpt()
images = [cv2.imread(file) for file in glob.glob("sample/*.jpg")]

#converting image to RGB system
images = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in images]

#get results from model in format:
#[{"label":"person", "confidence": 0.56, "topleft": {"x": 184, "y": 101}, "bottomright": {"x": 274, "y": 382}},
#{"label": "dog", "confidence": 0.32, "topleft": {"x": 71, "y": 263}, "bottomright": {"x": 193, "y": 353}},
#{"label": "horse", "confidence": 0.76, "topleft": {"x": 412, "y": 109}, "bottomright": {"x": 592,"y": 337}}]
results = [tfnet2.return_predict(img) for img in images]

label_filter = 'bike'
confidence_filter = 0.1

for index,result in enumerate(results):
    img = images[index]
    for ouputs in result:
        if(ouputs['label'] == label_filter and float(round(ouputs['confidence'], 3)) >  confidence_filter ):
            tl = (ouputs['topleft']['x'], ouputs['topleft']['y'])
            br = (ouputs['bottomright']['x'], ouputs['bottomright']['y'])
            label = ouputs['label']
            txt = label + " " + str(ouputs['confidence'])
            img = cv2.rectangle(img, tl, br, (0, 0, 255), 7)
            img = cv2.putText(img, txt , tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imwrite('images_out/' + 'out' + str(index) +'.jpg',img)
