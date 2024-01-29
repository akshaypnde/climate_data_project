# Climate Data Analysis Project

## Project Overview
This project aims to analyze and visualize climate data over the last 100 years. Utilizing open-source tools, the project encompasses data extraction, transformation, loading (ETL), and visualization to provide insights into global climate change patterns.

## Structure

- `airflow/` - Airflow DAGs for data orchestration.
- `dbt/` - dbt models for data transformation.
- `sql/` - SQL scripts for data manipulation and querying.
- `src/` - Source code for ETL processes.
- `api_connectors/` - Modules to connect to climate data APIs.
- `data_processing/` - Scripts for data cleaning and processing.
- `tests/` - Test cases for data integrity and ETL processes.
- `dashboards/` - Configurations and scripts for data visualization.
- `configs/` - YAML configurations for data sources.
- `docs/` - Project documentation.

## Data Sources

- [NOAA Climate Data Online](https://www.ncdc.noaa.gov/cdo-web/)
- [NASA's Climate Change Data](https://climate.nasa.gov/)
- [Global Historical Climatology Network](https://www.ncdc.noaa.gov/ghcn-daily-description)
- [World Bank Climate Data API](https://climateknowledgeportal.worldbank.org/download-data)

## Technologies Used

- **Programming Languages**: Python, SQL, YAML
- **ETL Tool**: Apache Airflow
- **Data Warehouse**: PostgreSQL
- **Data Transformation**: dbt (data build tool)
- **Dashboards and Reporting**: Apache Superset / Redash
- **Observability/Monitoring**: Prometheus and Grafana
- **Testing**: Pytest

## Getting Started

1. **Installation**: Clone this repository and install required dependencies.
2. **Configuration**: Set up the necessary configurations in the `configs/` directory.
3. **Running the ETL Process**: Instructions on initiating and scheduling ETL jobs.
4. **Dashboard Access**: Steps to access and interact with the dashboards.

## Testing

- Test scripts are located in the `tests/` directory.
- Run tests using Pytest to ensure data integrity and process accuracy.

## Observability

- Prometheus and Grafana are used for monitoring ETL jobs and data quality.

## Contributing

- Contributions to the project are welcome! Please refer to the `CONTRIBUTING.md` for guidelines.

## License

This project is licensed under the [MIT License](LICENSE.md) - see the LICENSE file for details.

## Contact

For any queries or contributions, please contact me.
