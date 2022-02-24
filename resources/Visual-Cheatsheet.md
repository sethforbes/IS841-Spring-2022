# Visual Cheatsheet

## Loading Data 

| Operator  | Name  |  Notes | 
|---|---|---|
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/read-csv.svg)  | Read CSV  | Can read csv files with an nice importer or from the Web  |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/read-excel.svg)  | Read Excel Worksheets  | Can select a sheet and set metadata  |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/retrieve.svg)  | Retrieve  | Retrieve data from a repostiory.  It's worth noting that you can load models or collections as well as datasets.  |


## Data Wrangling and Performance

| Operator  | Name  |  Notes | 
|---|---|---|
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/select-attributes.svg)  | Select Attributes  | You can select a single column, a subset of columns, or even by column data type (e.g. values)  |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/filter-examples.svg)  | Filter Examples  | Filter the rows of data.  One example might be to just remove all rows with missing data.  |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/set-role.svg)  | Set Role  | Manage the metadata for your dataset.  The primary use case is to set the role to `Label`, but you can also type-in the value, which is helpful to keep the columns but exclude from most modeling approaches.  |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/multiply.svg)  | Multiply  | This is a handy operator when you need to use an object (or state) many times. |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/write-csv.svg)  | Write CSV  | Save out text files to disk.  NOTE:  If you want a csv file, you need to change the sep argument to a `,` from a `';'. |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/numerical-to-polynominal.svg)  | Numeric to Polynominal  | Use this to change a numeric column that is categorically encoded (1,2,3) to a categorical column with many categories  |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/generate-attributes.svg)  | Generate Attributes  | Create new columns/features |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/blending-rename.svg)  | Rename  | Use this to rename columns.  NOTE:  There are other operators that can be used for bulk-changes (e.g. match a pattern)  |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/concurrency-join.svg)  | Join  | Blend datasets by joining the data on column(s) |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/replace-missing-values.svg)  | Replace Missing Values  | Replace missing values, including cateogrical data, with a fixed or calculated value.  Average is the mode for categorical data. |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/normalize.svg)  | Normalize  | Rescale the data to a specific ranage.  This can be 0/1 or a z-score, for example. |





## Modeling

> Individual models are not shown, but utilities to help with the modeling process overall.

| Operator  | Name  |  Notes | 
|---|---|---|
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/split-data.svg)  | Split Data  | Use this to create splits for your data.  Commonly used to create reproducible Train/Test splits. |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/apply-model.svg)  | Apply Model  | Use this operator to apply the model to a new set of data.  Note: Operators like `Normalize` are also Models; they are referred to as pre-processing models and have a `pre` name on the ouput port. |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/performance-classification.svg)  | Performance - Classification |  Performance metrics for classification models |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/performance-regression.svg)  | Performance Regression || Performance metrics for regression models |
| ![](https://docs.rapidminer.com/latest/studio/operators/img/operators/cluster-distance-performance.svg)  | Cluster Distance Performance  | This model can help you understand the performance of centroid-based (e.g. Kmeans) cluster models |


## Advanced Features

> These can help with performance considerations or help to evaluate a solution space.

| Operator  | Name  |  Notes | 
|---|---|---|
| ![](https://snipboard.io/UXiQLD.jpg)  | Caching Subprocess  | Double-click to build a sub-process.  The results will be cached after they are run and can dramatically improve the performance of your processes when used correctly. |
| ![](https://snipboard.io/O8lCPj.jpg)  | Loop Parameters  | The subprocess will run for each combination of parameter values that you specify.  This can be used to extract performance for a range of models in order to determine the "best" model |
| ![](https://docs.rapidminer.com/9.10/studio/operators/img/operators/append.svg)  | Append  | This operator can stack datasets.  This is helpful when looping/iterating through a set of steps. |
| ![](https://docs.rapidminer.com/9.10/studio/operators/img/operators/append.svg)  | Append  | This operator can stack datasets.  This is helpful when looping/iterating through a set of steps. |



