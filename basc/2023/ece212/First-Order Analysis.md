## Transient Analysis
- Initial System response to $\Delta$ 
- Dies off exponentially

## Steady-State Response
-  When Transients "die out" as $t\to\infty$

## First-Order Circuit 
- With just one storage element

## The following are continuous @ $t=0$
- Voltage for [[Capacitors]]
- Current for [[Inductors]]

## Analyzing these circuits in the form: ([[Homogenous Linear DEs]]):
$$\frac{dy}{dt}+\frac{y}{\tau}=0$$
Where $\tau=RC$.
## Our General Solution Will Look Like:
$$y=c_1e^{-\frac{1}{\tau}t}$$
Where $c_1$ will arise from the initial condition.

```mermaid
graph TD
    A[Bank Transaction Records] ---> B
    B[Data Ingestion] --> C[Feature Extraction]
    C --> D[Inference Formatting]
    D --> E(ML Prediction Model)
    E --> F[Bank Rec UI]
    F --> G[User Feedback]
    G -->|Modified Prediction Results| I[(Data Storage)]
    I -->|Training| E
    I --> B
    subgraph JJ[ETL]
	    B
	    C
	    D
	end

```

```mermaid
graph TD
    A[Bank Transaction Records] ----> B
    B[Data Ingestion] --> C1[Distributed Feature Extraction]
    C1 --> D1[Distributed Inference Formatting]
    E1(Distributed Prediction Model) --> F1[Bank Rec UI]
    F1 --> G1[User Feedback]
    G1 -->|Modified Prediction Results| I[(Data Storage)]
    I -->|Training| E1
    I --> B
    subgraph ETL
	    B
        C1
        D1
    end
    subgraph Cloud Infrastructure
        E1
        I
    end
    D1 -.->|API Gateway| Z[Load Balancer]
    Z --> E1


```

