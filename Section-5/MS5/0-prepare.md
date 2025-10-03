Nice — I’ll draft this clearly and practically using a retail example so everything maps to real constraints.

---

### Question 1 — Business scenario (50–100 words)

A regional retail chain faces persistent stockouts for fast-selling items and overstock for slow-moving SKUs across dozens of stores. The key problem is inaccurate demand forecasting and inefficient replenishment, which causes lost sales, higher carrying costs, and poor customer experience. Real-world implications include reduced revenue, wasted warehouse space, and strained supplier relationships. Principal constraints: scalability to many SKUs and stores, operational feasibility across legacy POS systems, and cost limits for compute and integration resources.

---

### Question 2 — Core problem & techniques (50–100 words)

Core problem: produce accurate, store-level demand forecasts and optimized replenishment plans that minimize stockouts and inventory costs. Relevant AI/ML techniques include time-series forecasting (e.g., gradient-boosted trees on engineered features, or sequence models like Temporal Fusion Transformer), probabilistic forecasting for demand uncertainty, and optimization (constrained linear/integer programming) for replenishment. Business requirements: low-latency predictions at daily cadence, integration with POS/ERP, and explainability for planners. Technical requirements: scalable training/inference, fault-tolerant pipelines, and secure access to sales data.

---

### Question 3 — Design the solution (400–550 words)

**Data collection and preprocessing**
Required data sources: historical POS sales (SKU × store × timestamp), inventory on-hand and receipts, promotions and markdown timelines, pricing history, supplier lead times, store attributes (size, demographics, local events), and external signals like weather and holidays. For real-time operation, ingest daily sales and inventory snapshots via batch ETL from POS/ERP; for higher responsiveness, add near-real-time streams (Kafka) for high-volume stores.

Preprocessing steps: unify timestamps and timezones, fill missing SKUs with zeros, align promotions and price changes to sales windows, and impute missing lead-time or store metadata using nearest-neighbor or median values. Normalize continuous features (log transform for skewed sales), encode categorical variables (target or embedding encodings for large SKU sets), and generate calendar features (day-of-week, holiday flags). Apply outlier filtering for data-entry spikes and create hierarchical aggregates (store-region, SKU-category) to mitigate sparse-level noise.

**Model selection**
Choose a hybrid approach: a probabilistic forecasting model per SKU-store using a Gradient Boosting Machine (e.g., LightGBM/CatBoost) on engineered lag, rolling-mean, promotion, and external features for baseline; supplement with a sequence model (Temporal Fusion Transformer) for complex seasonality and cross-series learning where data suffices. Probabilistic outputs (quantiles) are essential to capture uncertainty for replenishment. Use ensemble blending (weighted average) to improve robustness. For replenishment optimization, use a constrained optimization solver that consumes forecast quantiles, service-level targets, lead times, holding and stockout costs to compute order quantities.

Justification: GBMs scale well to many time series with engineered features and are computationally efficient; TFT captures temporal dependencies and shared patterns for cold-start SKUs. Probabilistic forecasts enable risk-aware ordering.

**Deployment strategy**
Host training pipelines and model artifacts in the cloud (managed Kubernetes or serverless ML platform). Use batch training daily and weekly full retrains using scalable compute (spot instances when safe). For inference: serve daily batch predictions via a scalable job (K8s CronJob or AWS Batch) writing to a forecast store (S3 + Redis cache). Expose a low-latency endpoint for on-demand forecasts via an autoscaled API gateway. Use load balancing and horizontal autoscaling to meet peak inference windows (start-of-day reorders).

**Cost optimization**
Minimize cost by: (1) using spot/commitment-based cloud instances for retraining, (2) batch inference during off-peak hours to leverage idle capacity, (3) caching forecasts for multiple consumers, and (4) pruning model complexity for less-critical SKUs (aggregate-level forecasts). Use serverless managed services where possible to reduce ops overhead.

**Monitoring and maintenance**
Monitor model metrics: MAE/SMAPE per SKU-store, prediction interval coverage (PI coverage), business KPIs like fill rate, days-of-inventory, and stockout rate. Track latency, throughput, and data pipeline health. Implement drift detection (statistical tests on feature distributions and residuals); trigger automated retraining or alerting when drift crosses thresholds. Maintain a retraining cadence (weekly incremental, monthly full) and a human-in-the-loop review for flagged SKUs. Log explanations (SHAP/feature importance) for planners to ensure transparency and trust.

---

If you want, I can convert this into a slide-ready summary or adapt it to a different domain (manufacturing predictive maintenance, smart-city energy, etc.). Which would you prefer?
