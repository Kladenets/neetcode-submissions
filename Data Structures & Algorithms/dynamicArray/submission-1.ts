class DynamicArray {
    _array: Array<number>;
    _currEnd: number;

    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity: number) {
        this._array = new Array(capacity);
        this._currEnd = 0;
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i: number): number {
        return this._array[i];
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i: number, n: number): void {
        this._array[i] = n;
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n: number): void {
        if (this._currEnd == this._array.length) {
            this.resize();
        }
        this._array[this._currEnd++] = n;
    }

    /**
     * @returns {number}
     */
    popback(): number {
        const toReturn = this._array[--this._currEnd];
        this._array[this._currEnd] = undefined;
        return toReturn;
    }

    /**
     * @returns {void}
     */
    resize(): void {
        this._array[(this._array.length * 2) - 1] = undefined;
    }

    /**
     * @returns {number}
     */
    getSize(): number {
        return this._currEnd;
    }

    /**
     * @returns {number}
     */
    getCapacity(): number {
        return this._array.length;
    }
}
