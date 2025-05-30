Overview
VectorShift Pipeline Builder is a React-based web application that enables users to design complex data processing pipelines using a visual, drag-and-drop interface. Inspired by visual programming tools, it allows users to connect various node types to create directed acyclic graphs (DAGs) that represent data workflows.

✨ Features
Interactive Node Canvas: Drag-and-drop interface for creating and connecting nodes
Multiple Node Types:
Basic: Input, Output, LLM, Text
Advanced: Data Processor, Database, API, Conditional, File
Dynamic Text Nodes: Auto-resize based on content with variable detection
Visual Variable Binding: Automatically creates input handles for variables in double curly braces
Pipeline Validation: Backend integration to verify DAG structure
Modern UI: Purple-themed interface with gradients, glows, and responsive design
🛠️ Tech Stack
Frontend
React
ReactFlow for node-based UI
Zustand for state management
Custom styling system
Backend
FastAPI for the API framework
NetworkX for graph analysis
Pydantic for data validation


📝 Usage
Drag nodes from the sidebar onto the canvas
Connect nodes by dragging from output handles to input handles
Configure nodes by filling in their properties
Use the Text node to create dynamic variables with {{variableName}} syntax
Click "Submit Pipeline" to validate your workflow
View the validation results showing node count, edge count, and DAG validity
