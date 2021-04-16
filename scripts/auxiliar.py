from tqdm import tqdm

def set_image_name(image_name, prefix=None):
    return f'{prefix}/{image_name}' if prefix else image_name


def get_image_features_df_from_file(file_path, dataframe, image_name_prefix=None):
    with open(file_path, 'r') as f:
        for line in tqdm(f):
            treated_line = line.replace('\n', '').strip()
            if treated_line.endswith('.jpg'):
                image_name = set_image_name(treated_line, image_name_prefix)
            else:
                features = treated_line.split('\t')
                dataframe.loc[len(dataframe), :] =\
                    (image_name_prefix, image_name, *features)
    return dataframe