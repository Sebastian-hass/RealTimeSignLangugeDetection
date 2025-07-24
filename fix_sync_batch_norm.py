import fileinput

file_path = r"C:\Users\ASUS\anaconda3\envs\tfod\lib\site-packages\object_detection\core\freezable_sync_batch_norm.py"
old_line = "class FreezableSyncBatchNorm(tf.keras.layers.experimental.SyncBatchNormalization):"
new_line = "class FreezableSyncBatchNorm(tf.keras.layers.SyncBatchNormalization):"

with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
    for line in file:
        if old_line in line:
            print(line.replace(old_line, new_line), end='')
        else:
            print(line, end='')

print("Cambio realizado correctamente.")