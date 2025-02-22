# Ceres Solver - A fast non-linear least squares minimizer
# Copyright 2017 Google Inc. All rights reserved.
# http://ceres-solver.org/
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of Google Inc. nor the names of its contributors may be
#   used to endorse or promote products derived from this software without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: sameeragarwal@google.com (Sameer Agarwal)
#
# Script for explicitly generating template specialization of the
# SchurEliminator class. It is a rather large class
# and the number of explicit instantiations is also large. Explicitly
# generating these instantiations in separate .cc files breaks the
# compilation into separate compilation unit rather than one large cc
# file which takes 2+GB of RAM to compile.
#
# This script creates two sets of files.
#
# 1. schur_eliminator_x_x_x.cc
# where, the x indicates the template parameters and
#
# 2. schur_eliminator.cc
#
# that contains a factory function for instantiating these classes
# based on runtime parameters.
#
# The list of tuples, specializations indicates the set of
# specializations that is generated.

# Set of template specializations to generate

HEADER = """// Ceres Solver - A fast non-linear least squares minimizer
// Copyright 2017 Google Inc. All rights reserved.
// http://ceres-solver.org/
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// * Redistributions of source code must retain the above copyright notice,
//   this list of conditions and the following disclaimer.
// * Redistributions in binary form must reproduce the above copyright notice,
//   this list of conditions and the following disclaimer in the documentation
//   and/or other materials provided with the distribution.
// * Neither the name of Google Inc. nor the names of its contributors may be
//   used to endorse or promote products derived from this software without
//   specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.
//
// Author: sameeragarwal@google.com (Sameer Agarwal)
//
// Template specialization of SchurEliminator.
//
// ========================================
// THIS FILE IS AUTOGENERATED. DO NOT EDIT.
// THIS FILE IS AUTOGENERATED. DO NOT EDIT.
// THIS FILE IS AUTOGENERATED. DO NOT EDIT.
// THIS FILE IS AUTOGENERATED. DO NOT EDIT.
//=========================================
//
// This file is generated using generate_template_specializations.py.
"""

DYNAMIC_FILE = """
#include "ceres/schur_eliminator_impl.h"

namespace ceres {
namespace internal {

template class SchurEliminator<%s, %s, %s>;

}  // namespace internal
}  // namespace ceres
"""

SPECIALIZATION_FILE = """
// This include must come before any #ifndef check on Ceres compile options.
#include "ceres/internal/port.h"

#ifndef CERES_RESTRICT_SCHUR_SPECIALIZATION

#include "ceres/schur_eliminator_impl.h"

namespace ceres {
namespace internal {

template class SchurEliminator<%s, %s, %s>;

}  // namespace internal
}  // namespace ceres

#endif  // CERES_RESTRICT_SCHUR_SPECIALIZATION
"""

FACTORY_FILE_HEADER = """
#include "ceres/linear_solver.h"
#include "ceres/schur_eliminator.h"

namespace ceres {
namespace internal {

SchurEliminatorBase::~SchurEliminatorBase() = default;

std::unique_ptr<SchurEliminatorBase> SchurEliminatorBase::Create(
    const LinearSolver::Options& options) {
#ifndef CERES_RESTRICT_SCHUR_SPECIALIZATION
"""

FACTORY = """  return std::make_unique<SchurEliminator<%s, %s, %s>>(options);"""

FACTORY_FOOTER = """
#endif
  VLOG(1) << "Template specializations not found for <"
          << options.row_block_size << "," << options.e_block_size << ","
          << options.f_block_size << ">";
  return std::make_unique<SchurEliminator<Eigen::Dynamic,
                                          Eigen::Dynamic,
                                          Eigen::Dynamic>>(options);
}

}  // namespace internal
}  // namespace ceres
"""
