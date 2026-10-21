---
layout: group
title: "WGMLEARN"
heading: "Working Group on Machine Learning in Marine Science"
tagline: "Pioneering the application of machine learning and artificial intelligence in marine research and ecosystem observation"

# Dynamic Sidebar Configuration
chairs:
  - name: "Ketil Malde"
    affiliation: "Institute of Marine Research (IMR)"
    country: "Norway"
    email: "ketil.malde@hi.no"
  - name: "Hassan Moustahfid"
    affiliation: "National Oceanic and Atmospheric Administration (NOAA)"
    country: "United States"
    email: "hassan.moustahfid@noaa.gov "

events:
  - date: "November, 2026"
    title: "WGMLEARN Annual Meeting"
    location: "Copenhagen, DE"
  - date: "December 04, 2026"
    title: "Hands-on Tutorial: Foundation Models (SAM+DINO)"
    location: "Online (GitHub Classroom)"
  - date: "February 22-26, 2027"
    title: "International Marine AI Hackathon"
    location: "Bergen, Norway"

quick_links:
  - text: "ICES WGMLEARN Official Page"
    url: "https://www.ices.dk/community/groups/Pages/WGMLEARN.aspx"
  - text: "ICES Data Portals"
    url: "https://www.ices.dk/data/data-portals/Pages/default.aspx"
  - text: "WGMLEARN GitHub Organization"
    url: "https://github.com/ices-eg/wgmlearn"
  - text: "WKAAII Workshop Page"
    url: "https://www.ices.dk/community/groups/Pages/WKAAII.aspx"

publications:
  - year: "2025"
    title: "WGMLEARN Annual Report 2024"
    citation: "ICES Scientific Reports, 6:92"
  - year: "2024"
    title: "A review of computer vision applications in marine science"
    citation: "ICES Journal of Marine Science, Vol 81"
  - year: "2023"
    title: "Establishing benchmark datasets for marine species classification"
    citation: "ICES Cooperative Research Report No. 359"
---

The **Working Group on Machine Learning in Marine Science (WGMLEARN)** serves as the interdisciplinary hub within the International Council for the Exploration of the Sea (ICES) for integrating Artificial Intelligence (AI) and Machine Learning (ML) into marine research.

We bring together marine scientists, data engineers, and ML researchers to solve complex ecological and resource-management challenges. As mainstream ML research focuses heavily on generic domains (like consumer photography and autonomous driving), WGMLEARN identifies, standardizes, and addresses the unique challenges encountered in the marine domain.

---

## Our Mission & Objectives

The field of AI and ML is developing at an unprecedented pace. WGMLEARN provides scientific leadership and technical guidance to ensure the ICES community can safely and robustly leverage these advanced technologies:
* **Advice & Guidance**: We provide comments, inputs, and guidance to other ICES expert groups on the application of machine learning.
* **Highlighting Marine-Specific Gaps**: We identify and highlight the unique technical challenges of marine data (e.g., poor light in underwater imaging, acoustic noise, high cost of annotation) that standard commercial AI models fail to address.
* **Benchmark Datasets**: We establish high-quality, open-access, and fully annotated training sets to steer mainstream ML research towards high-value opportunities in marine science and management.

---

## Terms of Reference (ToR) & Deliverables

WGMLEARN operates under a structured, three-year planning cycle. Our current core tasks and expected deliverables are:

| ToR | Description | Deliverables |
| :--- | :--- | :--- |
| **ToR A: Identify Challenges** | Develop a comprehensive list of AI/ML topics, task frameworks, and unmet challenges specific to the marine domain and potential benefits. Integrates output from WKAAII. | • A high-impact **Review Paper** in a "food-for-thought" format detailing marine ML bottlenecks. |
| **ToR B: Coordinate Groups** | Establish communication and coordinate with other ICES working groups, research groups, and databases to explore collaboration opportunities and chart user needs. | • A comprehensive **List of Networking Contacts** and database of active marine AI collaborators. |
| **ToR C: Organize Events** | Organize and execute 5–10 capacity-building events (tutorials, hackathons, workshops, and conference sessions) to target important challenges. | • **Tutorials**: Online learning modules and video recordings.<br>• **Hackathons**: Open-source code repositories (GitHub) and peer-reviewed manuscripts. |

---

## Highlights: Unmet Challenges in Marine ML

Under **ToR A**, we have categorized the critical areas where standard AI algorithms fall short and where specialized marine-focused research is required:

### 1. Labeling & Annotation Bottlenecks
Traditional deep learning models require millions of high-quality labels. In marine science, expert annotation of underwater camera imagery or acoustics is extremely slow and expensive.
* **The Marine Challenge**: High-volume, multi-modal, and hierarchical data (e.g., classifying plankton or complex benthic habitats with non-flat taxonomies).
* **Our Solutions**: Exploring Weakly-Supervised Learning, active learning, and leveraging zero-shot computer vision models like **SAM (Segment Anything)** and **DINO** to automate labeling pipelines.

### 2. Edge Computing & Robotics
To monitor the world's oceans in real-time, AI models must be deployed directly on battery-powered robots or remote systems with highly limited internet access.
* **The Marine Challenge**: Managing fleets of autonomous platforms (AUVs, USVs, gliders). Deploying compact, energy-efficient algorithms for real-time edge processing on satellites, drones, and LiDAR sensors.
* **Our Solutions**: Compression techniques, model quantization, and self-optimizing deployment pipelines.

### 3. Physics-Informed & Hybrid Modeling
Purely data-driven ML models are prone to generating physically impossible predictions when presented with out-of-distribution marine data.
* **The Marine Challenge**: Extremely limited sample sizes under edge conditions (e.g., rare species or extreme weather events).
* **Our Solutions**: Merging physical/oceanographic/mechanistic models with data-driven ML (e.g., continuous 3D acoustic distributions, Anemoi/NERSC models) to enforce conservation laws.

### 4. Marine Foundation Models
General-purpose language or image models do not understand oceanography, acoustics, or taxonomic structures.
* **The Marine Challenge**: Constructing specialized foundation models trained specifically on marine data.
* **Our Solutions**: Developing pre-trained foundation models for species identification and acoustic spectrograms (e.g., the *AqQua* project for plankton).

---

## Get Involved with WGMLEARN

WGMLEARN is an active, open, and collaborative community. Whether you are an AI/ML specialist, a marine ecologist, or an offshore software engineer, your skills are needed to steer the future of Marine AI.

* Check out our **Quick Links** on the sidebar to explore our repositories, databases, and community channels.
* Contact the Working Group Chairs directly to inquire about participating in our next annual meeting, joining an upcoming hackathon, or co-authoring a tutorial!
