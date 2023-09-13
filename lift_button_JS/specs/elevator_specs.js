import assert from "assert";
import Elevator from "../models/Elevator.js"


describe("Elevator", function() {
    let elevator

    beforeEach(function() {
        elevator = new Elevator()
    })
    
    it('should light up when off, doors are closed', function() {
        const actual = elevator.pressLiftButton()
        assert.ok(actual)
    })

    it('should stay lit when on, doors closed', function() {
        const actual = elevator.pressLiftButton()
        assert.ok(actual)
        const actual2 = elevator.pressLiftButton()
        assert.ok(actual)
    })

    it('should not light up when off, doors are open', function() {
        elevator.openDoors()
        const actual = elevator.pressLiftButton()
        assert.strictEqual(actual, false)
    })

    it('should turn light off when doors open', function() {
        elevator.pressLiftButton()
        const actual = elevator.getLights()
        assert.strictEqual(actual, true)
        elevator.openDoors()
        const actual2 = elevator.getLights()
        assert.strictEqual(actual2, false)
    })
})