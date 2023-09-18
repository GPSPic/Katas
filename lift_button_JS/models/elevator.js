class Elevator {
    constructor() {
        this.lightOn = false
        this.doorsOpen = false
    }

    getLights() {
        return this.lightOn
    }

    openDoors() {
        this.doorsOpen = true
        this.lightOn = false
    }

    closeDoors() {
        this.doorsOpen = false
    }
    
    pressLiftButton() {
        if (!this.doorsOpen) {
            this.lightOn = true
        }
    
        return this.lightOn
    }
}



export default Elevator