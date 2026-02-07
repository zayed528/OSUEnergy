df = spark.read.csv(
    "/Volumes/workspace/default/osu-energy-analysis/DATA I-O 2026 Advanced Datasets/advanced_bonus/advanced_bonus/meter-readings-nov-2025.csv",
    header=True
)

display(df)
