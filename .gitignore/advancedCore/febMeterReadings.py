df = spark.read.csv(
    "/Volumes/workspace/default/osu-energy-analysis/DATA I-O 2026 Advanced Datasets/advanced_core/advanced_core/meter-readings-feb-2025.csv",
    header=True
)

display(df)
