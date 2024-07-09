# Realtime Digital Filter Design

This project is a desktop application designed to assist users in creating custom digital filters through zeros-poles placement on the z-plane. Implemented using Python and PyQt5, the application provides an interactive interface for filter design and real-time signal processing.

## Features

### 1. Interactive Z-Plane Plot
The core of the application is the interactive z-plane plot, which includes:
- **Placing Zeros and Poles**: Users can click on the plot to place zeros and poles. These elements are essential for defining the characteristics of the digital filter.
- **Modifying Zeros and Poles**: Dragging allows users to adjust the positions of zeros and poles, providing a dynamic way to tweak filter parameters.
- **Deleting Elements**: Users can click on a zero or pole to delete it, enabling easy correction of mistakes or adjustments.
- **Conjugate Addition**: For complex elements, users have the option to add conjugates automatically, simplifying the design of symmetric filters.

### 2. Frequency Response Visualization
As users interact with the z-plane plot, the application provides real-time updates of the filter's frequency response:
- **Magnitude Response**: Displays how the amplitude of the filter varies with frequency.
- **Phase Response**: Shows how the phase of the filter varies with frequency.
These visualizations help users understand the impact of their design choices on the filter's performance.

### 3. Real-Time Signal Filtering
The application supports applying the designed filter to a real-time signal:
- **Filtering a Lengthy Signal**: Users can load a signal with at least 10,000 points and observe how the filter processes it over time.
- **Adjustable Processing Speed**: A slider allows users to control the speed of the filtering process, from processing 1 point per second to 100 points per second, or any rate in between.
- **Signal Visualization**: The application plots both the original and filtered signals, showing the filtering progress in real-time.

### 4. User-Generated Real-Time Signals
Users can create real-time signals by moving the mouse on a designated area:
- **Mouse Movement Input**: The x- or y-coordinate of the mouse generates the input signal.
- **Frequency Control**: Faster mouse movements create higher frequency signals, while slower movements create lower frequency signals.

### 5. Phase Correction with All-Pass Filters
To correct phase distortions introduced by the filter, the application includes a library of all-pass filters:
- **All-Pass Filter Library**: Users can browse and visualize the zero-pole combinations and phase responses of predefined all-pass filters.
- **Custom All-Pass Filters**: If the library filters are insufficient, users can create custom all-pass filters by specifying parameters.
- **Enable/Disable All-Pass Filters**: Users can selectively enable or disable added all-pass filters through a drop-down menu or checkboxes, allowing for fine-tuning of the filter design.

## Installation

To run this application, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/omarrrefaatt/realtime-digital-filter-design.git
    cd realtime-digital-filter-design
    ```

2. Run the application:
    ```bash
    python main.py
    ```

## Usage

### Placing and Modifying Zeros and Poles
- **Placing**: Click on the z-plane plot to add a zero or pole.
- **Modifying**: Drag the placed zeros or poles to new positions as needed.
- **Deleting**: Right-click on a zero or pole to remove it.
- **Adding Conjugates**: Use the provided option to add conjugate pairs for complex zeros and poles.

### Visualizing Frequency Response
- The application displays the magnitude and phase responses of the filter in real-time as you modify the z-plane plot.
- Use these visualizations to adjust the filter design for the desired frequency characteristics.

### Real-Time Signal Filtering
- **Loading a Signal**: Load a signal file to apply the filter.
- **Adjusting Speed**: Use the slider to control the processing speed of the filter.
- **Viewing Results**: The application plots the original and filtered signals, showing the effects of the filter in real-time.

### Generating Real-Time Signals
- **Mouse Input**: Move the mouse in the designated area to generate real-time input signals.
- **Frequency Control**: Adjust the speed of mouse movement to control the signal frequency.

### Phase Correction with All-Pass Filters
- **Browsing the Library**: Explore the provided all-pass filters and visualize their characteristics.
- **Creating Custom Filters**: Define custom all-pass filters if the library filters are insufficient.
- **Enabling/Disabling Filters**: Use the interface to enable or disable selected all-pass filters to achieve the desired phase correction.

## Screenshots
<img width="1200" alt="Screenshot 2024-07-09 at 6 25 55 PM" src="https://github.com/omarrrefaatt/Realtime-Digital-Filter-Design-/assets/119802537/16e9b68e-e94b-4ba1-8d10-0cd1206072c6">

---
<img width="1204" alt="Screenshot 2024-07-09 at 6 17 16 PM" src="https://github.com/omarrrefaatt/Realtime-Digital-Filter-Design-/assets/119802537/02f6fc12-7c95-44ec-b327-3276d62dc3a7">


---
<img width="1201" alt="Screenshot 2024-07-09 at 6 17 53 PM" src="https://github.com/omarrrefaatt/Realtime-Digital-Filter-Design-/assets/119802537/c8a64423-30d7-4d88-9676-172d719fef9a">


## Contributing


1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgments

- [EarLevel Engineering](https://www.earlevel.com) for inspiration and resources on digital filter design.

---
