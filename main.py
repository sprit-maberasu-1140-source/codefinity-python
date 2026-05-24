import pandas as pd
# 1. pandas ライブラリを pd という名前で読み込みます

def filter_large_csv(input_file, output_file, column, threshold, chunk_size=10000):
    # 2. 関数定義：入力ファイル、出力ファイル、列名、閾値、チャンクサイズを受け取る

    filtered_chunks = []
    # 3. 条件を満たしたチャンクをためておくリストを初期化

    for chunk in pd.read_csv(input_file, chunksize=chunk_size):
        # 4. 指定サイズずつ CSV を分割読み込み

        filtered = chunk[chunk[column] > threshold]
        # 5. 各チャンクで、指定列の値が閾値を超える行だけを抽出

        if not filtered.empty:
            # 6. 抽出結果が空でなければ
            filtered_chunks.append(filtered)
            # 7. 結果リストに追加

    if filtered_chunks:
        # 8. １つ以上チャンクがたまっていれば
        result = pd.concat(filtered_chunks)
        # 9. リスト内のすべてのチャンクを縦方向に結合

        result.to_csv(output_file, index=False)
        # 10. 結合結果を出力ファイルに書き出し（行番号は含めない）
    else:
        # 11. 条件に合う行が１件もなかったとき
        pd.read_csv(input_file, nrows=0).to_csv(output_file, index=False)
        # 12. 元ファイルのヘッダーだけを出力

# --- サンプル呼び出し ---
input_file  = "https://.../large_file.csv"
output_file = "filtered_output.csv"
column      = "value"
threshold   = 100

try:
    filter_large_csv(input_file, output_file, column, threshold)
except Exception as e:
    print(str(e))
    # エラー発生時はメッセージを表示