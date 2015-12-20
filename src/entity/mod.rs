#![allow(dead_code)]
use std::rc::Rc;
use std::ops::{
    Add,
    Sub,
};
use chunk::{ChunkOption};

pub struct Vec3f64 {
    x: f64,
    y: f64,
    z: f64,
}

pub struct Entity {
    mass: Rc<ChunkOption>,
    velocity: Vec3f64,
    location: Vec3f64,
    rotation: Vec3f64,
}

impl Add<Vec3f64> for Vec3f64 {
    type Output = Vec3f64;
    fn add(self, _rhs: Vec3f64) -> Vec3f64 {
        Vec3f64 {
            x: self.x + _rhs.x,
            y: self.y + _rhs.y,
            z: self.z + _rhs.z
        }
    }
}

impl Sub<Vec3f64> for Vec3f64 {
    type Output = Vec3f64;
    fn sub(self, _rhs: Vec3f64) -> Vec3f64 {
        Vec3f64 {
            x: self.x + _rhs.x,
            y: self.y + _rhs.y,
            z: self.z + _rhs.z
        }
    }
}

