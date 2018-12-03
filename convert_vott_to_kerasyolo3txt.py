import json
import os


def convert_vott_to_kerasyolo3txt(json_path, image_dir, train_txt_save_path, classes_txt_save_path):

    row_list = []

    with open(json_path) as f:
        dic = json.load(f)
        tag_set = set()

        visited_frames = dic['visitedFrames']

        frames = dic['frames']
        frame_keys = frames.keys()

        for visited in visited_frames:
            if visited in frame_keys:  # framesに存在するkeyのみ
                img_annotation_list = frames[visited]
                for item in img_annotation_list:
                    tags = item['tags']
                    for t in tags:
                        tag_set.add(t)

        tag_dic = {}
        tag_list = list(tag_set)
        tag_list.sort()
        for i, tag in enumerate(tag_list):
            tag_dic[tag] = i

        for visited in visited_frames:
            if visited in frame_keys:  # framesに存在するkeyのみ
                img_annotation_list = frames[visited]

                row_text = os.path.join(image_dir, visited)

                for item in img_annotation_list:
                    box = item['box']
                    tags = item['tags']

                    for tag in tags:
                        row_text = row_text + ' {},{},{},{},{}'.format(int(box['x1']),int(box['y1']),int(box['x2']),int(box['y2']), int(tag_dic[tag]))

                if len(img_annotation_list) != 0:
                    row_list.append(row_text)

    train_txt = '\n'.join(row_list)

    print(train_txt)

    f = open(train_txt_save_path, 'w')
    f.write(train_txt)
    f.close()

    classes_txt = '\n'.join(tag_list)

    f = open(classes_txt_save_path, 'w')
    f.write(classes_txt)
    f.close()


def _main():
    json_path = '../resize_images.json'  # VoTTのアノテーション情報が記録されたjsonファイルのパス
    image_dir = '../resize_images/'  # 画像が保存されたディレクトリのパス
    train_txt_save_path = 'my_train.txt'  # keras-yolo3で学習に使うアノテーション情報が記録されたテキストファイルの保存先のパス
    classes_txt_save_path = 'model_data/my_classes.txt' # keras-yolo3で学習に使うラベルの記録

    convert_vott_to_kerasyolo3txt(
        json_path=json_path,
        image_dir=image_dir,
        train_txt_save_path=train_txt_save_path,
        classes_txt_save_path=classes_txt_save_path
    )

if __name__ == '__main__':
    _main()

